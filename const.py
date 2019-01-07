LINES_DIVIDER = "|\n"
HTML_START = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.title {
  background-color: #444;
  color: white;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 18px;
  font-family: "Verdana";
  white-space: pre-wrap;
}
.title:hover {
  background-color: #333;
}
.collapsible {
  background-color: #777;
  color: white;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
  font-family: "Verdana";
  white-space: pre-wrap;
}
.active, .collapsible:hover {
  background-color: #555;
}
.collapsible:after {
  content: "+";
  color: white;
  font-weight: bold;
  float: right;
  margin-left: 5px;
}
.active:after {
  content: "-";
}
.content {
  padding: 0 18px;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.2s ease-out;
  background-color: #f1f1f1;
  font-family: "Verdana";
  white-space: pre-wrap;
}
</style>
</head>
<body>
"""
HTML_STOP = """
<script>
var coll = document.getElementsByClassName("collapsible");
var i;
for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    } 
  });
}
</script>

</body>
</html>
"""
HTML_COL1 = '<button class="collapsible">'
HTML_COL2 = '</button>'
HTML_COL3 = '<div class="content"><p>'
HTML_COL4 = '</p></div>'
HTML_COL5 = '<div class="title"><p>'
HTML_COL6 = '</p></div>'
