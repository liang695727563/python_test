'''
数据压缩
以下模块直接支持通用的数据打包和压缩格式：zlib, gip, bz2, zipfile, 以及 tarfile。

'''
import zlib
s = b'withch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

print(zlib.decompress(t))

print(zlib.crc32(s))