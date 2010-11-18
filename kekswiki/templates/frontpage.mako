<%inherit file="base.mako"/>

<article>
    <h1>List of all pages in this instance of Kekswiki</h1>
    <section>
        <ul id="titles">
        % for title in c.titles:
            <li>
                <a href="${h.url_for(controller='article', title=title, action='index')}">
                    ${title}
                </a>
        % endfor
        </ul>
    </section>
</article>
