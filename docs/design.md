# blo
## What is this?
**blo** is my blog engine utility for posts.
### Process outline
1. Read markdown file
2. Convert to html
3. Write to database and convert from that main section to "wakachi-gaki" style format.
### About Wakachi-gaki
"wakachi-gaki" is simple way for full text search in Japanese text.
It split word by spaces.

ex)
`私はプログラミングが好きです ==> 私 は プログラミング が 好きです`

## Command Line and how to use
`$ blo [file.md]`
1. set blo to git hook (git push hook).
2. write my article on markdown format.
3. git commit and git push of my article.
4. git hook execute blo, it convert to article to database information.

## Table structure
Database backend are SQLite3 (with FTS4).
main table structure is below:
- id : key column, auto increment
- text : article's main text, it converted html format
- digest : check sum (sha512) digest of main text (with html tags)
- updatedate : last update date (timestamp: yyyy/mm/dd hh:nn:ss)

And it contains virtual table for full text search.

**DDL:**
```sqlite
CREATE TABLE `Articles` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`text`	TEXT,
	`digest`	TEXT UNIQUE,
	`updatedate`	TEXT
);

CREATE VIRTUAL TABLE Articles_fts USING fts4( words TEXT );
```

## Depending packages
- SQLite3 (with Full text search option)
- MeCab (with ipa dictionary)

Please see,  `requirements.txt`

## Other
- html convert function is powered by CommonMarkdown.py
- full text search depend on SQLite.
