<h2>DOCUMENTATION</h2><br><br>

<b>Functionalities:</b><br>
1. Text indexing and search.<br>
2. Image indexing and search.<br>
3. PDF file indexing and search.<br>


<b>Programming Language used: Python</b><br>

URL: https://mighty-peak-57343.herokuapp.com/<br>

The "/sample inputs/" folder contains the sample images and text and a pdf file which were used to test the web app.<br>


<h3>How to Use:</h3>
A we go to the link above, it lands us to one of the two pages:<br>
 -   Main search page (If the index is already built)<br>
 -   Index building page (If the index is not built or has been cleared)<br>



<b>The main search page</b> has these components:
         - An input bar to input text (word in this case).<br>
         - A "Submit Query" button which when clicked shows the results of the searched query on the page itself<br>
         - An "INDEX A DOCUMENT" button, which when clicked, takes to a separate page built for indexing text and pdf docs.<br>
         - A "CLEAR INDEX" button that clears the index when clicked.<br>
         - An "IMAGE SEARCH ENGINE" that takes to the image search page.<br>
The index documents page contains a text-area for inputting text that is to be indexed. Below that, it has a File upload widget that lets us upload a pdf file and when clicking "Submit File" button, it uploads the file to the sever and it is indexed. The search results now will also include the text from the pdf file.<br><br>


<h3>The IMAGE SEARCH ENGINE:</h3>
On clicking the "IMAGE SEARCH ENGINE" button on the main search page, it takes the user to a new page in a new window. <br>
The image search page has the following components: <br>
--A single image upload widget on the top left side accompanied by a "SEARCH SIMILAR IMAGES" button. Here we can browse an image from our computer and on clicking the button, it will fetch similar images form backend and show them below the horizontal line.<br>
--A multiple image upload widget on the top right side accompanied by a "INDEX IMAGES" button. This lets us select multiple images from our computer and upload them. After uploading their features are extracted at the backend and then saved to the index.<br>


<h3>PERFORMANCE AND LATENCY:</h3>
---The text index and search feature is really fast.<br>
---Tested on my local machine with Intel I5 8th generation processor (Octa core) and integrated graphics, the image search takes about 0.005 seconds to fetch results from a huge database of images, <b>which is really quick.</b><br>
---On Heroku, the free tier only includes <b>1 GB of RAM and a comparatively slower and  weaker processor with less number pf cores</b>. This leads to a little increase in latency for image search, as compared to my local computer. But the Algorithms are optimized. <br><br>


<b>SNAPSHOTS OF THE APP:</b><br>

 

 <img src="/app snapshots/Screenshot (46).png"> </img>
 
 <img src="/app screenshots/Screenshot (41).png"> </img>
The image search <br>




<img src="/app screenshots/Screenshot (48).png"> </img>
The text search <br>




<img src="/app screenshots/Screenshot (55).png"> </img>
The text index page<br>



