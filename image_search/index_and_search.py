# this module has helper functions to save, index and search images
import cv2
import numpy as np
import os
import pickle
from image_search.extract_features import FeatureExtractorClass



class ImageSearch:
    
    def __init__(self):
        # here we load the saved index. And build an index if saved index isn't found
        self.fe = FeatureExtractorClass((3,12,8))
        self.image_index = np.empty((0,1440))
        self.image_names = []
        if os.path.isfile("image_search/imagesindex/index"):
            with open("image_search/imagesindex/index" ,"rb") as file:
                self.image_index = pickle.load(file) # numpy array of images features. Shape= (number of images , feature_size)
            with open("image_search/imagesindex/names",'rb') as file:
                self.image_names = pickle.load(file) # list of image names
            print("Index loaded from disk.")
        else:
            self.index_images_from_gallery()
        # initializing the feature extractor class
        
    
    def index_image(self, imagename, image, directory=None):
        # this function takes in an imagename (string) and an image numpy array
        if directory:
            # then all the images inside the folder must be indexed
            for imagename in os.listdir(directory):
                image_vector = np.array(self.fe.vectorize(cv2.imread(os.path.join(directory, imagename)))) # gives a numpy array of length 1440
                self.image_index = np.vstack([self.image_index, image_vector])
                self.image_names.append(imagename)
            with open("index","wb") as file:
                pickle.dump(self.image_index , file)
            with open("names","wb") as file:
                pickle.dump(self.image_names, file)
        else:
            image_vector = self.fe.vectorize(image) # gives a numpy array of length 1440
            self.image_index = np.vstack([self.image_index, image_vector])
            self.image_names.append(imagename)
            print("SHAPE OF IMAGE INDEX NOW: ", self.image_index.shape)
            # now serializing it to disk with pickle
            with open("index","wb") as file:
                pickle.dump(self.image_index , file)
            with open("names","wb") as file:
                pickle.dump(self.image_names, file)
    
    def index_images_from_gallery(self):
        print("GENERATING IMAGE INDEXES FROM IMAGES PRESENT IN GALLERY...")
        path = r"C:\Users\Yugal\Documents Previous lappy\django-test\TapSearch App\tapsearch\static\images"
        self.index_image(None,None, directory=path)
        print("Images already in the storage have been indexed.")
        
    def chi2_distance(self, A, eps = 1e-10):
       # Chi squared distance works better than Euclidian distance for Histograms, hence...
       # this function returns the CHI squared dist for the given vector with each of the vectors in the index
       diff_sq = (A - self.image_index)**2
       addition = (A + self.image_index) + eps
       division = diff_sq / addition # element wise division
       print(division.shape)
       # now sum up accross columns
       summation = np.sum(division, axis=-1)
       print(summation.shape)
       distances = summation * 0.5
       return distances
    
    def search_image(self, image=None, imagepath=None,topn=10):
        if imagepath:  # absolute path with name
            image = cv2.imread(imagepath)
        vector = self.fe.vectorize(image)
        # now we find its distances from all the other vectors in the index
        distances = self.chi2_distance(vector)
        distances = [(distances[i], self.image_names[i]) for i in range(distances.shape[0])]
        # now sort the distances and then return the top n images names.
        final = []
        i=0
        for k in sorted(distances): # by default the key for sorting is the element at index 0 for each entry in the iterable
            i += 1
            final.append(k)
            if i >= topn:
                break
        return final
    
    

#        
#IS = ImageSearch()
#answers = IS.search_image(imagepath=r"C:\\Users\\Yugal\\Documents Previous lappy\django-test\\TapSearch App\\tapsearch\\image_search\\queries\\103300.png")
#
#
#
#
#path = r"C:\Users\Yugal\Documents Previous lappy\django-test\TapSearch App\tapsearch\static\images"
#for k in answers:
#    img = cv2.imread(os.path.join(path, k[1]))
#    cv2.imshow("",img)
#    cv2.waitKey(0)


