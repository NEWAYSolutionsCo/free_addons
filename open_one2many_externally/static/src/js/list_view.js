odoo.define('open_one2many_externally.list_view', function (require) {
"use strict";

var ListRenderer = require('web.ListRenderer');

return ListRenderer.include({

    /**
     * Main render function for the list.  It is rendered as a table. For now,
     * this method does not wait for the field widgets to be ready.
     *
     * @override
     * @private
     * returns {Deferred} this deferred is resolved immediately
     */
    _renderView: function () {
        var self = this;

        var $rows = this._super();

        this.$el
            .removeClass('table-responsive')
            .empty();

        // destroy the previously instantiated pagers, if any
        _.invoke(this.pagers, 'destroy');
        this.pagers = [];

        var displayNoContentHelper = !this._hasContent() && !!this.noContentHelp;
        // display the no content helper if there is no data to display
        if (displayNoContentHelper) {
            this.$el.html(this._renderNoContentHelper());
            return this._super();
        }

        var $table = $('<table>').addClass('o_list_view table table-sm table-hover table-striped');
        this.$el.addClass('table-responsive')
            .append($table);
        this._computeAggregates();
        $table.toggleClass('o_list_view_grouped', this.isGrouped);
        $table.toggleClass('o_list_view_ungrouped', !this.isGrouped);
        this.hasHandle = this.state.orderedBy.length === 0 ||
            this.state.orderedBy[0].name === this.handleField;
        if (this.isGrouped) {
            $table
                .append(this._renderHeader(true))
                .append(this._renderGroups(this.state.data))
                .append(this._renderFooter());
        } else {
            $table
                .append(this._renderHeader())
                .append(this._renderBody())
                .append(this._renderFooter());
        }

        if (typeof this.isMany2Many !== 'undefined'){

            var $table_external_btn = $(
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
            
            this.$el.prepend($table_external_btn);

        }

        if (this.selection.length) {
            var $checked_rows = this.$('tr').filter(function (index, el) {
                return _.contains(self.selection, $(el).data('id'));
            });
            $checked_rows.find('.o_list_record_selector input').prop('checked', true);
        }
        return $rows;
    },
    
});

});
