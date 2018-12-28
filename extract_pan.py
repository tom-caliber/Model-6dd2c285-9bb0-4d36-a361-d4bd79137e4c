import os
import pickle
import io
import re
from google.cloud import vision

__author__ = 'mohak'

#export GOOGLE_APPLICATION_CREDENTIALS=/Users/div/Documents/zygmo/expts/syg_pan/gCloud.json
path_response_dir = 'cld_resp/'

def detect_text(path_name):
    """Detects text in the file."""

    file_name = os.path.splitext(os.path.basename(path_name))[0]
    resp_file_name = os.path.join(path_response_dir, file_name) + ".pkl"

    if os.path.isfile(resp_file_name):
        print('Local cache')
        response = pickle.load(open(resp_file_name, "rb"))
    else:
        client = vision.ImageAnnotatorClient()
        print('Client activated')
        with io.open(path_name, 'rb') as image_file:
            content = image_file.read()
        image = vision.types.Image(content=content)
        response = client.text_detection(image=image)
        pickle.dump(response, open(resp_file_name, "wb"))
    return(response)


def get_pan(path_name):
    cld_resp = detect_text(path_name)
    #print (cld_resp)
    texts = cld_resp.text_annotations
    #print(texts)
    # print('Texts:')
    for text in texts:
        #print(text.description)
        #print('----')
        #print('\n"{}"'.format(text.description))
        #vertices = (['({},{})'.format(vertex.x, vertex.y)
        # for vertex in text.bounding_poly.vertices])
        #print('bounds: {}'.format(','.join(vertices)))
        #print "-----" + str(re.match(r'[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}', text.description))
        if re.match(r'[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}', text.description) is not None:
            #print re.search(r'[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}', text.description)
            print(text.description)

if __name__ == "__main__":
    get_pan('imgs/1.jpg')
    get_pan('imgs/2.jpg')
    get_pan('imgs/3.jpg')
    get_pan('imgs/4.jpg')
    get_pan('imgs/5.jpg')
    get_pan('imgs/6.jpg')
    get_pan('imgs/7.jpg')
    get_pan('imgs/8.jpg')
