<p align="center">
  <img width="480" height="360" src="https://github.com/yezz123/Cryptoggy/blob/master/img/Lookpad.gif">
</p>
<p align="center"><img src="https://img.shields.io/badge/Version-1.0-brightgreen"></p>

</p> 
<p align="center"><img src="https://img.shields.io/badge/Author-Yezz123-green.svg"> 
</p>


<p align="center">
  <a href="https://github.com/yezz123">
    <img src="https://img.shields.io/github/followers/yezz123?label=Follow&style=social">
  </a>
  <a href="https://github.com/yezz123/Cryptoggy/stargazers">
    <img src="https://img.shields.io/github/stars/yezz123/Cryptoggy?style=social">
  </a>
</p>

# Cryptoggy:

  Cryptoggy is an open source, fully python ransomware PoC. It's main purpose is
not to be run like most software projects, but to be read for educational
purposes.

Aside from very minor testing to ensure there are no syntax errors, no testing
has been done. This may occur at a later time to ensure it performs in all
expected environments,but that is not the point. The point is to be a simple
to read PoC that makes for an easy example of what ransomware is and how it
works. And hopefully, this can lead to a better understanding of ransomware in 
the network defense and sysadmin communities.

## Why?

There is a severe lack of open source ransomware, and for good reason! But by
having so few examples, and those examples being inaccurate (intentionally bad
code with flaws), or just too complicated, it doesn't leave much to analyze
and learn from. People seem to think that ransomware is hard to write. That
it's this complex, hard to develop, hard to RE, and hard to prevent beast. A
quick read through of this codebase will prove that's not true. Im hoping this
can lead to better signatures, a better understanding of how ransomware works
and what can be done to stop it, and an overall safer internet.

 ## Extensions:
 ```python
  def discoverFiles(startpath):
    
    extensions = [
        'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw', # images
        'mp3','mp4', 'm4a', 'aac','ogg','flac', 'wav', 'wma', 'aiff', 'ape', # music and sound
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp', # Video and movies

        'doc', 'docx', 'xls', 'xlsx', 'ppt','pptx', # Microsoft office
        'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', # OpenOffice, Adobe, Latex, Markdown, etc
        'yml', 'yaml', 'json', 'xml', 'csv', # structured data
        'db', 'sql', 'dbf', 'mdb', 'iso', # databases and disc images

        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css', # web technologies
        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', # C source code
        'java', 'class', 'jar', # java source code
        'ps', 'bat', 'vb', # windows based scripts
        'awk', 'sh', 'cgi', 'pl', 'ada', 'swift', # linux/mac based scripts
        'go', 'py', 'pyc', 'bf', 'coffee', # other source code files

        'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',  # compressed formats
    ]
```    
## Objections!

But aren't you worried someone will abuse it for profit?

- Not really. There are plenty of much better, more advanced ransomware out there.
 Even if they do, it's hopefully few compared to the good it will do.

But when they do, it would be your fault!

- Nope! I only wrote it. I didnt deploy it, I didnt sell it, it's not my
problem. Hopefully nobody uses it for evil but thats the price to be paid for
good. There's always someone who will do it.

But...

- Alright. Bottom line. Security is a very reactive business. To make the
world more secure you first have to make it less secure. To make better AV and
signatures, you must first make better malware. And that's what we're doing
here.

<code> **Warning: This project is young and incomplete. It will encrypt and decrypt
files. That's about it. No key generation, no sending the key back over a
secure channel, no dropping new files or wallpapers or whatever. I'll get to
that. Maybe. Open an issue if you so desire, pull requests welcome.** </code>

<p align="center">
    <a href="https://yassertahiri.medium.com/">
    <img alt="Medium" src="https://img.shields.io/badge/Medium%20-%23000000.svg?&style=for-the-badge&logo=Medium&logoColor=white"/></a>
    <a href="https://twitter.com/THyasser1">
    <img alt="Twitter" src="https://img.shields.io/badge/Twitter%20-%231DA1F2.svg?&style=for-the-badge&logo=Twitter&logoColor=white"</a>
    <a href="https://discord.gg/crNvkTYPYG">
    <img alt="Discord" src="https://img.shields.io/badge/Discord%20-%237289DA.svg?&style=for-the-badge&logo=discord&logoColor=white"/></a>
</p>

<p align="center"><a href="https://github.com/yezz123/Cryptoggy#"><img src="http://randojs.com/images/backToTopButton.png" alt="Back to top" height="29"/></a></p>
