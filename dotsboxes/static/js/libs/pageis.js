/*
* pageis.js
* 
* ----------------------------------------------
* author: Yasar ICLI
* version: 3.0
* 
* Use the Tacirnet
*
* Sample:

        var base_methods = { plugin1: function() { }, plugin2: function() {} }
        new Page({
        
            "PublicPlugin": function() {
            
                Plugin(); 

                // methods perm ? 
                this.PublicPluginjQuery(); <-- 
            },

            "PublicPluginjQuery": function() {
            
                jQuery("#div").plugin();
            }

        }, base_methods).is("Index", function(pagename, methods) {
        
            // @publicPlugin
            O.PublicPlugin();

        })("Category", function(pagename, methods) {
        
            // @publicPlugin
            O.PublicPlugin();

            // @PublicPluginjQuery
            O.PublicPluginjQuery();
        })("AllPage", function() {
        
            console.log("All Page functionss...");
        });


        2.0 V added window methods.
        ########## IndexId.methodname() in window ##########
            pageid=Category;
            
                Category.PublicPlugin();
                Category.PublicPluginjQuery();
                Category.plugin1();
                Category.plugin2();
*/

var Page = (function(methods, base_methods) {

    // Object this as self
    var self = this,

        /*
        * 
        * .getAttribute html id as html_id 
        */
        html_id = document.getElementsByTagName("html")[0].getAttribute("id");


    // @default {Object} methods.["Main function"] 
    (methods || (methods == {}));
    (base_methods || (base_methods == {}));

    /*
    *
    * Private extends function methods and base_methods
    *
    * @param {object} destination
    * @param {object} source
    */ 
    var _extend = (function(destination, source) {
        
        for (var property in source) (function() {
        
            destination[property] = source[property];
        }());
        return destination; 
    });



    /*
    *
    * has(["1", 2, "hello"], "hello") --> true
    */
    var has = function(list, search){ return list.indexOf(search)!=-1 };

    /*
    *
    * Object new methods merge --^^
    * 
    *   {
    *       methods, base_methods
    *   } 
    */
    self.methods = _extend(methods, base_methods);


    /*
    *
    * Page is used to assign special functions. as well as 
    * the methods used can.
    * 
    * Sample:
    *   Pageid=Index && methods a, b, c
    *   Index.a();
    *   Index.b();
    *   Index.c();
    */
    for (var method in self.methods) (function(key, value) {

        // @keys_name --> html_id.keys_name();
        var keys_name = (html_id + "_" + method);

        // @setWindow keys_name = value (key, value)
        window[keys_name] = value;
    }(method, self.methods[method]));


    /*
    *
    * if html_id == pagename then run callback recursive methods.
    *
    * PageIs("Index", function() {}).PageIs("Category", function() {});
    * 
    * @param {String} pagename is html id
    * @param {function} callback is html_id == pagename then run callback
    */
    self.Is = (function(pagenames, callback) { 

        // @defaultParam {function} callback
        (callback || (callback == function() {}));


        // @set attribute object [pagename, callback]
        self.pagenames = pagenames;
        self.callback = callback;

        var or = pagenames.split("|");
        if (has(or, html_id) || has(or, "*") || has(or, "AllPage")) (function() {
            
            // @callback
            callback(html_id, self.methods, or);
        }());

        /*
        *
        * return self.Is new method curry style  
        *
        * (pagename, callback)(pagename, callback)(pagename, callback)
        */
        return (self.Is);
    });


    /*
    *
    * if self.pagename and seşf.callback is Empty then not new object undefined
    * else return cury style. 
    */
    if (self.pagenames && self.callback) (function() {
    
        self.Is(self.pagenames, self.callback);
    }());
});
