## Batch add tags according to the specified vocabulary list.

<img src="image\gfgdfgherghdf.png" alt="gfgdfgherghdf" style="zoom:67%;" />

Only tested in Anki Version ⁨2.1.61

The python version used is 3.11.3

----

**Find the plugin in the plugin options to modify the configuration**

<img src="image\jgj645635345.png" alt="jgj645635345" style="zoom:67%;" />



<img src="image\fgfegesdfg.png" alt="fgfegesdfg" style="zoom: 50%;" />

```
{
  "field_name": "expression",
  "tag_name": "COCA-2W",
  "words_path": "E:\\wordsFrequency\\COCA-2W.txt"
}
```

----

**"field_name"** contains the word to look for, change according to note type.



<img src="image\gdhsdgfh.png" alt="gdhsdgfh" style="zoom: 67%;" />



**"tag_name"** is the tag to be added.



**"words_path"** is the local directory of the vocabulary file, using the txt file format, each word is on a separate line.

<img src="image\20230420191842046.png" alt="20230420191842046" style="zoom:60%;" />



**The format of the path string can be either of the following two:**

```
"words_path": "E:\\wordsFrequency\\COCA-2W.txt"
"words_path": "E:/wordsFrequency/COCA-2W.txt"
```



