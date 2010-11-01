<%inherit file="base.mako"/>

<article>
    <h1>${c.title}</h1>
    <nav>
        <a class="edit-link" href="${h.url_for(title=c.title, action='edit')}">Edit</a>
    </nav>
    <section>
        ${h.sanitize_html(c.content) | n}
    </section>
</article>
