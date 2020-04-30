# import the necessary packages
from pyzbar import pyzbar
import cv2
import time
import os
start = time.time()
def main():
    images = []
    folder = r'F:\project\XMLAlgoService\Barcode_reading\barcodes_images'
    for filename in os.listdir(folder):
            try:
                # print folder loc
                print(folder + '\\' + filename)

                # read the image in to memory
                image = cv2.imread(folder + '\\' + filename)

                # call decode and get the barcodes
                barcodes = pyzbar.decode(image)

                # loop over the detected barcodes
                for barcode in barcodes:
                    # extract the bounding box location of the barcode and draw the
                # bounding box surrounding the barcode on the image
                    (x, y, w, h) = barcode.rect
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

                    # the barcode data is a bytes object so if we want to draw it on
                    # our output image we need to convert it to a string first
                    barcodeData = barcode.data.decode("utf-8")
                    barcodeType = barcode.type

                    # draw the barcode data and barcode type on the image
                    text = "{} ({})".format(barcodeData, barcodeType)
                    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 0, 255), 2)

                    # print the barcode type and data to the terminal
                    print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

                # show the output image
                cv2.imshow(filename, image)

            except:
                print('Cant import ' + filename)

    # show the output image
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    end = time.time()
    print(end - start)
if __name__=="__main__":
    main()