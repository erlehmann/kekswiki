<%inherit file="base.mako"/>

<h1>${c.title}</h1><strong>Edit</strong>
<nav>
    <a class="view-link" href="${h.url_for(title=c.title, action='index')}">View</a>
</nav>

${h.form(h.url_for(action='preview'), method='get')}
    <textarea id="article-text" name="article-text" cols="80" rows="${len(c.content)/60}">${c.content}</textarea>
    ${h.submit('preview', 'Preview')}
${h.end_form()}

