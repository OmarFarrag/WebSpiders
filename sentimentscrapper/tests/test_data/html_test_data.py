class HtmlTestData():

    sub_categories_html = {
        """
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
