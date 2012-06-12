import json

from pyramid.i18n import get_locale_name

DEFAULT_SETTINGS = {
    u'allow_captioned_images': False,
    u'atd_ignore_strings': u'Zope,Plone,TinyMCE',
    u'atd_rpc_id': u'Products.TinyMCE-admin',
    u'atd_rpc_url': u'${application_url}/',
    u'atd_show_types': u'Bias Language,Cliches,Complex Expression,Diacritical Marks,Double Negatives,Hidden Verbs,Jargon Language,Passive voice,Phrases to Avoid,Redundant Expression',
    u'autoresize': False,
    u'body_class': u'documentContent',
    u'body_id': u'content',
    u'buttons': [u'save',
                 u'style',
                 u'bold',
                 u'italic',
                 u'justifyleft',
                 u'justifycenter',
                 u'justifyright',
                 u'justifyfull',
                 u'bullist',
                 u'numlist',
                 u'definitionlist',
                 u'outdent',
                 u'indent',
                 u'image',
                 u'link',
                 u'unlink',
                 u'anchor',
                 u'tablecontrols',
                 u'code',
                 u'fullscreen',
                 u''],
    u'content_css': u'${application_url}/static-kotti-tinymce/content.css',
    u'contextmenu': True,
    u'customplugins': [u'kottibrowser'],
    u'directionality': u'ltr',
    u'document_base_url': u'${base_url}',
    u'document_url': u'${context_url}',
    u'entity_encoding': u'raw',
    u'fix_list_elements': False,
    u'gecko_spellcheck': True,
    u'image_shortcuts_html': [u'\n<img src="img/home.png" />\n<a id="home" href="${application_url}">Home</a>\n',
                              u'\n<img src="img/folder_current.png" />\n<a id="currentfolder" href="${context_url}">Current Folder</a>\n'],
    u'inlinepopups_skin': u'plonepopup',
    u'labels': {u'label_addnewfile': u'Add new File',
                u'label_addnewimage': u'Add new Image',
                u'label_browseimage': u'Image Browser',
                u'label_browselink': u'Link Browser',
                u'label_browser': u'Browser',
                u'label_internal_path': u'You are here:',
                u'label_lists': u'Lists',
                u'label_no_anchors': u'No anchors in this page',
                u'label_no_items': u'No items in this folder',
                u'label_paragraph': u'Normal paragraph',
                u'label_plain_cell': u'Plain cell',
                u'label_print': u'Print',
                u'label_search_results': u'Search results:',
                u'label_selection': u'Selection',
                u'label_shortcuts': u'Shortcuts',
                u'label_style_ldots': u'Style...',
                u'label_styles': u'(remove style)',
                u'label_tables': u'Tables',
                u'label_text': u'Text'},
    u'language': u'en',
    u'link_shortcuts_html': [u'\n<img src="img/home.png" />\n<a id="home" href="${application_url}">Home</a>\n',
                             u'\n<img src="img/folder_current.png" />\n<a id="currentfolder" href="${context_url}">Current Folder</a>\n'],
    u'link_using_uids': False,
    u'livesearch': True,
    u'media_strict': False,
    u'mode': u'exact',
    u'navigation_root_url': u'${application_url}/',
    u'num_of_thumb_columns': 4,
    u'plugins': u'advhr,definitionlist,directionality,emotions,fullscreen,inlinepopups,insertdatetime,media,nonbreaking,noneditable,pagebreak,paste,plonebrowser,ploneinlinestyles,plonestyle,preview,print,save,searchreplace,tabfocus,table,visualchars,xhtmlxtras,contextmenu',
    u'portal_url': u'${application_url}/',
    u'rooted': False,
    u'script_url': u'http://localhost:8080/Plone/front-page/tiny_mce_gzip.js',
    u'skin': u'plone',
    u'table_firstline_th': True,
    u'table_styles': u'Invisible grid=invisible;Fancy listing=listing;Fancy grid listing=grid listing;Fancy vertical listing=vertical listing',
    u'theme': u'advanced',
    u'theme_advanced_buttons1': u'save,style,bold,italic,justifyleft,justifycenter,justifyright,justifyfull,bullist,numlist,definitionlist,outdent,indent',
    u'theme_advanced_buttons2': u'image,link,unlink,anchor,tablecontrols,code,fullscreen',
    u'theme_advanced_buttons3': u'',
    u'theme_advanced_buttons4': u'',
    u'theme_advanced_path': False,
    u'theme_advanced_path_location': u'bottom',
    u'theme_advanced_resize_horizontal': False,
    u'theme_advanced_resizing': True,
    u'theme_advanced_resizing_use_cookie': True,
    u'theme_advanced_source_editor_height': 400,
    u'theme_advanced_source_editor_width': 600,
    u'theme_advanced_styles': u'[{ title: "Text", tag: "", className: "-", type: "Text" },{ title: "Normal paragraph", tag: "p", className: "-", type: "Text" },{ title: "Heading", tag: "h2", className: "-", type: "Text" },{ title: "Subheading", tag: "h3", className: "-", type: "Text" },{ title: "Literal", tag: "pre", className: "-", type: "Text" },{ title: "Pull-quote", tag: "blockquote", className: "pullquote", type: "Text" },{ title: "Call-out", tag: "p", className: "callout", type: "Text" },{ title: "Clear floats", tag: "div", className: "visualClear", type: "Text" },{ title: "Selection", tag: "", className: "-", type: "Selection" },{ title: "(remove style)", tag: "", className: "-", type: "Selection" },{ title: "Discreet", tag: "span", className: "discreet", type: "Selection" },{ title: "Highlight", tag: "span", className: "visualHighlight", type: "Selection" },{ title: "Tables", tag: "table", className: "-", type: "Tables" },{ title: "Plain cell", tag: "td", className: "-", type: "Tables" },{ title: "Invisible grid", tag: "table", className: "invisible", type: "Tables" },{ title: "Fancy listing", tag: "table", className: "listing", type: "Tables" },{ title: "Fancy grid listing", tag: "table", className: "grid listing", type: "Tables" },{ title: "Fancy vertical listing", tag: "table", className: "vertical listing", type: "Tables" },{ title: "Odd row", tag: "tr", className: "odd", type: "Tables" },{ title: "Even row", tag: "tr", className: "even", type: "Tables" },{ title: "Heading cell", tag: "th", className: "-", type: "Tables" },{ title: "Lists", tag: "ul", className: "-", type: "Lists" },{ title: "Lists", tag: "ol", className: "-", type: "Lists" },{ title: "Lists", tag: "dl", className: "-", type: "Lists" },{ title: "Lists", tag: "dl", className: "-", type: "Lists" },{ title: "Disc", tag: "ul", className: "listTypeDisc", type: "Lists" },{ title: "Square", tag: "ul", className: "listTypeSquare", type: "Lists" },{ title: "Circle", tag: "ul", className: "listTypeCircle", type: "Lists" },{ title: "Numbers", tag: "ol", className: "listTypeDecimal", type: "Lists" },{ title: "Lower Alpha", tag: "ol", className: "listTypeLowerAlpha", type: "Lists" },{ title: "Upper Alpha", tag: "ol", className: "listTypeUpperAlpha", type: "Lists" },{ title: "Lower Roman", tag: "ol", className: "listTypeLowerRoman", type: "Lists" },{ title: "Upper Roman", tag: "ol", className: "listTypeUpperRoman", type: "Lists" },{ title: "Definition term", tag: "dt", className: "-", type: "Lists" },{ title: "Definition description", tag: "dd", className: "-", type: "Lists" },{ title: "Print", tag: "", className: "-", type: "Print" },{ title: "Page break (print only)", tag: "div", className: "pageBreak", type: "Print" }]',
    u'theme_advanced_toolbar_align': u'left',
    u'theme_advanced_toolbar_location': u'top',
    u'thumbnail_size': [u'thumb', 64, 64],
    u'toolbar_width': 440,
    u'valid_elements': u'code[class|dir|id|style|title],kbd[class|dir|id|style|title],aside[class|dir|id|style|title],img[align|alt|class|dir|height|hspace|id|ismap<ismap|longdesc|name|src|style|title|usemap|vspace|width],title[dir|id],tt[class|dir|id|style|title],tr[align|char|charoff|class|dir|id|style|title],li[class|dir|id|style|title|type],source[class|dir|id|style|title],tfoot[align|char|charoff|class|dir|id|style|title],th[abbr|align|axis|char|charoff|class|colspan|dir|headers|id|nowrap|rowspan|scope|style|title],td[abbr|align|axis|char|charoff|class|colspan|dir|headers|id|nowrap|rowspan|scope|style|title],dl[class|compact|dir|id|style|title],blockquote[cite|class|dir|id|style|title],big[class|dir|id|style|title],dd[class|dir|id|style|title],meter[class|dir|id|style|title],dt[class|dir|id|style|title],small[class|dir|id|style|title],output[class|dir|id|style|title],div[align|class|dir|id|style|title],em[class|dir|id|style|title],datalist[class|dir|id|style|title],hgroup[class|dir|id|style|title],meta[content|dir|http-equiv|id|name|scheme],video[class|dir|id|style|title],rt[class|dir|id|style|title],canvas[class|dir|id|style|title],rp[class|dir|id|style|title],sub[class|dir|id|style|title],bdo[class|dir|id|style|title],sup[class|dir|id|style|title],progress[class|dir|id|style|title],body[alink|background|class|dir|id|link|style|text|title|vlink],acronym[class|dir|id|style|title],base[href|id|target],br[class|clear|id|style|title],address[class|dir|id|style|title],article[class|dir|id|style|title],strong[class|dir|id|style|title],ol[class|compact|dir|id|style|title|type],caption[align|class|dir|id|style|title],dialog[class|dir|id|style|title],col[align|char|charoff|class|dir|id|span|style|title|width],h2[align|class|dir|id|style|title],h3[align|class|dir|id|style|title],h1[align|class|dir|id|style|title],h6[align|class|dir|id|style|title],h4[align|class|dir|id|style|title],h5[align|class|dir|id|style|title],header[class|dir|id|style|title],table[align|class|dir|id|style|summary|title],#p[align|class|dir|id|style|title],span[class|dir|id|style|title],area[accesskey|alt|class|coords|dir|href|id|nohref|shape|style|tabindex|target|title],mark[class|dir|id|style|title],dfn[class|dir|id|style|title],var[class|dir|id|style|title],cite[class|dir|id|style|title],thead[align|char|charoff|class|dir|id|style|title],head[dir|id|profile],hr[align|class|dir|id|noshade|size|style|title|width],ruby[class|dir|id|style|title],b[class|dir|id|style|title],colgroup[align|char|charoff|class|dir|id|span|style|title|width],keygen[class|dir|id|style|title],ul[class|compact|dir|id|style|title|type],del[cite|class|datetime|dir|id|style|title],pre[class|dir|id|style|title|width],figure[class|dir|id|style|title],ins[cite|class|datetime|dir|id|style|title],tbody[align|char|charoff|class|dir|id|style|title],html[dir|id|xmlns],nav[class|dir|id|style|title],details[class|dir|id|style|title],u[class|dir|id|style|title],samp[class|dir|id|style|title],map[class|dir|id|name|title],a[accesskey|charset|class|coords|dir|href|hreflang|id|name|rel|rev|shape|style|tabindex|target|title|type],footer[class|dir|id|style|title],i[class|dir|id|style|title],q[cite|class|dir|id|style|title],command[class|dir|id|style|title],time[class|dir|id|style|title],audio[class|dir|id|style|title],section[class|dir|id|style|title],abbr[class|dir|id|style|title]',
    u'valid_inline_styles': u'text-align,list-style-type,float,padding-left',
    }


def replace_urls(value, request):
    base_url = context_url = request.resource_url(request.context).rstrip('/')
    application_url = request.application_url
    if context_url != application_url:
        base_url = base_url + '/'
    value = value.replace("${application_url}", application_url)
    value = value.replace("${context_url}", context_url)
    value = value.replace("${base_url}", base_url)
    return value


def get_settings_json(request):
    settings = DEFAULT_SETTINGS.copy()
    settings['language'] = get_locale_name(request)
    settings_json = json.dumps(settings)
    return replace_urls(settings_json, request)
