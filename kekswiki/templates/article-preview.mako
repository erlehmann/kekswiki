<%inherit file="base.mako"/>

<article>
    <h1>${c.title}</h1><strong>Preview</strong>
    <nav>
        <a class="edit-link" href="${h.url_for(title=c.title, action='edit')}">Edit</a>
        <a class="view-link" href="${h.url_for(title=c.title, action='index')}">View</a>
    </nav>

    <section>
        ${h.sanitize_html(c.content) | n}
    </section>
</article>

${h.form(h.url_for(action='commit'), method='post')}
    <input id="article-text" name="article-text" type="hidden" value="${c.content}" required>

    <label for="author-name">Author</label>
    <input id="author-name" name="author-name" type="text" required>        

    <label for="author-email">Author Email</label>
    <input id="author-email" name="author-email" type="email" required>

    <label for="message">Commit Message</label>
    <input id="message" name="message" type="text" required>

    ${h.submit('commit', 'Commit')}
${h.end_form()}

