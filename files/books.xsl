<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="/">
    <html>
      <body>
        <h2>Book List</h2>
        <ul>
          <xsl:for-each select="books/book">
            <li><xsl:value-of select="title"/> - <xsl:value-of select="author"/> (<xsl:value-of select="year"/>)</li>
          </xsl:for-each>
        </ul>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
