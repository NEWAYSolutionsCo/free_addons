odoo.define('open_one2many_externally.list_view', function (require) {
"use strict";

var ListRenderer = require('web.ListRenderer');

return ListRenderer.include({

    /**
     * Main render function for the list.  It is rendered as a table. For now,
     * this method does not wait for the field widgets to be ready.
     *
     * @override
     * @returns {Promise} resolved when the view has been rendered
     */
     async _renderView() {
        var self = this;
        const oldPagers = this.pagers;
        let prom;
        let tableWrapper;
        if (this.state.count > 0 || !this.noContentHelp) {
            // render a table if there are records, or if there is no no content
            // helper (empty table in this case)
            this.pagers = [];

            const orderedBy = this.state.orderedBy;
            this.hasHandle = orderedBy.length === 0 || orderedBy[0].name === this.handleField;
            this._computeAggregates();

            const $table = $(
                '<table class="o_list_table table table-sm table-hover table-striped"/>'
            );
            $table.toggleClass('o_list_table_grouped', this.isGrouped);
            $table.toggleClass('o_list_table_ungrouped', !this.isGrouped);
            const defs = [];
            this.defs = defs;
            if (this.isGrouped) {
                $table.append(this._renderHeader());
                $table.append(this._renderGroups(this.state.data));
                $table.append(this._renderFooter());

            } else {
                $table.append(this._renderHeader());
                $table.append(this._renderBody());
                $table.append(this._renderFooter());
            }
            tableWrapper = Object.assign(document.createElement('div'), {
                className: 'table-responsive',
            });

            if (typeof this.isMany2Many !== 'undefined'){

                const $table_external_btn = $(
                    '<div class="table_external_btn float-right pb-4"></div>'
                );

                $table_external_btn.append(
                    $(`<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/>
                            <polyline points="15 3 21 3 21 9"/>
                            <line x1="10" y1="14" x2="21" y2="3"/>
                        </svg>`
                    )
                );

                $table_external_btn.click(function(event) {
                    var modelName = self.state.model;
                    var res_ids = self.state.res_ids;
                    self.do_action({
                        name: self.arch.attrs.string || '',
                        type: 'ir.actions.act_window',
                        res_model: modelName,
                        target: 'current',
                        view_type: 'list',
                        views: [[false, 'list'], [false, 'form']],
                        domain: [['id', 'in', res_ids]],
                    });
                });

                tableWrapper.append($table_external_btn[0]);

            }

            tableWrapper.appendChild($table[0]);
            delete this.defs;
            prom = Promise.all(defs);
        }

        await Promise.all([this._super.apply(this, arguments), prom]);

        this.el.innerHTML = "";
        this.el.classList.remove('o_list_optional_columns');

        // destroy the previously instantiated pagers, if any
        oldPagers.forEach(pager => pager.destroy());

        // append the table (if any) to the main element
        if (tableWrapper) {
            this.el.appendChild(tableWrapper);
            if (document.body.contains(this.el)) {
                this.pagers.forEach(pager => pager.on_attach_callback());
            }
            if (this.optionalColumns.length) {
                this.el.classList.add('o_list_optional_columns');
                this.$('table').append(
                    $('<i class="o_optional_columns_dropdown_toggle fa fa-ellipsis-v"/>')
                );
                this.$el.append(this._renderOptionalColumnsDropdown());
            }
            if (this.selection.length) {
                const $checked_rows = this.$('tr').filter(
                    (i, el) => this.selection.includes(el.dataset.id)
                );
                $checked_rows.find('.o_list_record_selector input').prop('checked', true);
                if ($checked_rows.length === this.$('.o_data_row').length) { // all rows are checked
                    this.$('thead .o_list_record_selector input').prop('checked', true);
                }
            }
        }

        // display the no content helper if necessary
        if (!this._hasContent() && !!this.noContentHelp) {
            this._renderNoContentHelper();
        }
    },
    
});

});
