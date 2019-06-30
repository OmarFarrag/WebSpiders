class HtmlTestData():

    sub_categories_html = {
        """
        <li>
            <span>
                <h4> Hello </h4>
            </span>
        </li>
        <li>
            <span class="a-list-item">
                <a class="a-link-normal s-ref-text-link" href="b?ie=whatever">
                    <span class="a-size-small a-color-base">
                        Kids' Home Store
                    </span>
                </a>
            </span>
        </li>
    """:
        ["b?ie=whatever"],
    ##############################
        """
    
    <body>
        <li>
            <span>
                <h4> Hello </h4>
            </span>
        </li>
        <li>
            <span>
                <h4> Hello </h4>
            </span>
        </li>
        <li>
            <span class="a-list-item">
                <a class="a-link-normal s-ref-text-link" href="b?ie=whatever">
                    <span class="a-color-base">
                        Kids' Home Store
                            <a href="b?ie=notExtracted"></a>
                    </span>
                </a>
            </span>
        </li>
    </body>
    
    """:   ["b?ie=whatever"],
    ##############################
        """
        <li>
            <span>
                <h4> Hello </h4>
            </span>
        </li>
        <li>
            <span class="a-list-item">
                <span>
                <a class="a-link-normal s-ref-text-link" href="b?ie=notExtracted">
                    <span class="a-size-small a-color-base">
                        Kids' Home Store
                    </span>
                </a>
                </span>
            </span>
        </li>
    """: [],
    ##############################
        """
    <html>
        <li>
            <span>
                <h4> Hello </h4>
            </span>
        </li>
        <li>
            <span class="a-list-item">
                <a class="a-link-normal s-ref-text-link" href="/s/ref=lp_1622501101">
                    <span class="a-size-small a-color-base">
                        Kids' Home Store
                    </span>
                </a>
            </span>
        </li>
    </html>
    """: [],
    ##############################
        """
    <html>
        <li>
            <span>
                <h4> Hello </h4>
            </span>
        </li>
        <li>
            <span class="a-list-item">
                <a class="a-link-normal s-ref-text-link" href="/s/ref=lp_1622501101">
                    <span >
                        Kids' Home Store
                    </span>
                </a>
            </span>
        </li>
    </html>
    """: []
    }

    products_links = {
        """
        <div class="s-search-results" >
        <div></div>
            <a href="pass">
            <span><div></div></span></a>
        </div>
        """:
        ["pass"],

        """
        <div class="s-search-results" >
        <div></div>
            <span>
                <a href="not-passing"></a>
            </span>
            <ul>
                <li>
                    <a href="pass1">
                    <span></span></a>
                </li>
            </ul>
            <a href="pass2">
                    <span></span></a>
        </div>
        """:
        ["pass1","pass2"],

        """
        <div class="search-results" >
        <div></div>
            <span>
                <a href="none1"></a>
            </span>
            <ul>
                <li>
                    <a href="none"></a>
                </li>
            </ul>
        </div>
        """:
        [],
        """
        <div class="s-search-results" >
        <div></div>
            <span>
                <a href="none">
                </a>
            </span>
            <ul>
                <li>
                    <a href="pass2"></a>
                </li>
            </ul>
        </div>
        """:
        []
    }
