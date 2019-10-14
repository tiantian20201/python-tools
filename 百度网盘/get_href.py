"""
使用word文档的宏，代码如下：

Sub 提取超链接()
'
' 提取超链接 宏
'
'
For Each aHyperlink In ActiveDocument.Hyperlinks

With Selection

.InsertAfter aHyperlink.Name

.Collapse Direction:=wdCollapseEnd

.InsertParagraphAfter

End With

Next aHyperlink

End Sub


"""