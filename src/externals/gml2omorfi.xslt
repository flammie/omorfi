<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:gml="http://opengis.net/gml" 
    xmlns:names="http://xml.nls.fi/geographic-names/2019/02">
  <xsl:output method="text"/>



  <xsl:template match="gml:FeatureCollection">
      <xsl:apply-templates select="gml:featureMember"/>
  </xsl:template>

  <xsl:template match="gml:featureMember">
      <xsl:apply-templates select="names:Place"/>
  </xsl:template>

  <xsl:template match="names:Place">
      <xsl:apply-templates select="names:name"/>
  </xsl:template>

  <xsl:template match="names:name">
      <xsl:apply-templates select="names:Name"/>
  </xsl:template>

  <xsl:template match="names:Name">
      <xsl:apply-templates select="names:spelling"/>
      <xsl:text>_</xsl:text><xsl:apply-templates select="names:language"/>
      <xsl:text>&#xa;</xsl:text>
  </xsl:template>

</xsl:stylesheet>
