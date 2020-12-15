"""
@file: 附件URL提取测试
@author: DJZ
@time: 2020/12/08
@desc
"""

import re

my_html = "<p>附件:<ul id=udesk_attachments'><li><a href='https://pro-cs.kefutoutiao.com/tid44157/%E6%B5%8B%E8%AF%95_1607051996_1607051996097_b95dcb.png?OSSAccessKeyId=bPexlr6MCcadDhfu&Expires=1638588003&Signature=Lmux0QmU0RruKsQYeXiSkHQcy9Y%3D' download='测试_1607051996_1607051996097_b95dcb.png'>测试_1607051996_1607051996097_b95dcb.png</a></li><li><a href='https://pro-cs.kefutoutiao.com/tid44157/%E6%B5%8B%E8%AF%95_1607052000_1607052000292_a3d28d.docx?OSSAccessKeyId=bPexlr6MCcadDhfu&Expires=1638588003&Signature=ZFFqWNckfAvImbA7fE%2FpBB0vw48%3D' download='测试_1607052000_1607052000292_a3d28d.docx'>测试_1607052000_1607052000292_a3d28d.docx</a></li></ul></p>"

pattern = re.compile(r'href=\'(.*?)\'')
result = pattern.findall(my_html)
print(result[1])