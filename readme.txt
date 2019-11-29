DOCUMENTATION

Functionalities:
1. Text indexing and search.
2. Image indexing and search.
3. PDF file indexing and search.


Programming Language used: Python

URL: https://mighty-peak-57343.herokuapp.com/

The "/sample inputs/" folder contains the sample images and text and a pdf file which were used to test the web app.


How to Use:
A we go to the link above, it lands us to one of the two pages:
 -   Main search page (If the index is already built)
 -   Index building page (If the index is not built or has been cleared)



The main search page has these components:
         - An input bar to input text (word in this case).
         - A "Submit Query" button which when clicked shows the results of the searched query        on the page itself
         - An "INDEX A DOCUMENT" button, which when clicked, takes to a separate page built for indexing text and pdf docs.
         - A "CLEAR INDEX" button that clears the index when clicked.
         - An "IMAGE SEARCH ENGINE" that takes to the image search page.
The index documents page contains a text-area for inputting text that is to be indexed. Below that, it has a File upload widget that lets us upload a pdf file and when clicking "Submit File" button, it uploads the file to the sever and it is indexed. The search results now will also include the text from the pdf file.


The IMAGE SEARCH ENGINE:
On clicking the "IMAGE SEARCH ENGINE" button on the main search page, it takes the user to a new page in a new window. 
The image search page has the following components: 
A single image upload widget on the top left side accompanied by a "SEARCH SIMILAR IMAGES" button. Here we can browse an image from our computer and on clicking the button, it will fetch similar images form backend and show them below the horizontal line.
A multiple image upload widget on the top right side accompanied by a "INDEX IMAGES" button. This lets us select multiple images from our computer and upload them. After uploading their features are extracted at the backend and then saved to the index.


PERFORMANCE AND LATENCY:
The text index and search feature is really fast.
Tested on my local machine with Intel I5 8th generation processor (Octa core) and integrated graphics, the image search takes about 0.005 seconds to fetch results from a huge database of images, which is really quick.
On Heroku, the free tier only includes 1 GB of RAM and a comparatively slower and  weaker processor with less number pf cores. This leads to a little increase in latency for image search, as compared to my local computer. But the Algorithms are optimized. 


SNAPSHOTS OF THE APP:

 

 
The image search



 
The text search


 
The text index page




