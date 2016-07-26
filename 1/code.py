# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）
import random, string
def gene_code(count, length):
    res = set()
    while len(res) < count:
        res.add(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length)))
    return res

if __name__ == "__main__":
    res = gene_code(200, 8)
    f = open("code", 'w')
    f.write("\n".join(res))
    f.close()