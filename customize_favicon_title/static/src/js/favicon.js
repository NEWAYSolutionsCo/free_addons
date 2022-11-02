odoo.define('customize_favicon_title.favicon', function (require) {
"use strict";

var Favicon = require('web.AbstractWebClient');
var rpc = require('web.rpc');

return Favicon.include({

    init: function (parent) {
        this._super(parent);
        
        this.set('title_part', {"zopenerp": "NEWAY Solutions"});
    },

});

});
