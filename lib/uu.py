import cv2

class BoundingBoxWidget(object):
    def __init__(self, image_path):
        self.original_image = cv2.imread(image_path)
        self.clone = self.original_image.copy()

        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.extract_coordinates)

        # Bounding box reference points
        self.image_coordinates = []

    def extract_coordinates(self, event, x, y, flags, parameters):
        # Record starting (x,y) coordinates on left mouse button click
        if event == cv2.EVENT_LBUTTONDOWN:
            self.image_coordinates = [(x, y)]

        # Record ending (x,y) coordinates on left mouse button release
        elif event == cv2.EVENT_LBUTTONUP:
            self.image_coordinates.append((x, y))
            #print('top left: {}, bottom right: {}'.format(self.image_coordinates[0], self.image_coordinates[1]))
            #print('x,y,w,h : ({}, {}, {}, {})'.format(self.image_coordinates[0][0], self.image_coordinates[0][1], self.image_coordinates[1][0] - self.image_coordinates[0][0], self.image_coordinates[1][1] - self.image_coordinates[0][1]))

            # Draw rectangle
            cv2.rectangle(self.clone, self.image_coordinates[0], self.image_coordinates[1], (36, 255, 12), 2)
            cv2.imshow("image", self.clone)

        # Clear drawing boxes on right mouse button click
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.clone = self.original_image.copy()

    def show_image(self):
        return self.clone

    def get_coordinates(self):
        return self.image_coordinates if len(self.image_coordinates) == 2 else None

def main(image_path):
    boundingbox_widget = BoundingBoxWidget(image_path)
    while True:
        cv2.imshow('image', boundingbox_widget.show_image())
        key = cv2.waitKey(1)

        # Close program with keyboard 'q'
        if key == ord('q'):
            global coordinates
            coordinates = boundingbox_widget.get_coordinates()
            #if coordinates:
            #    print("Bounding Box Coordinates:")
            #    print("Top-left:", coordinates[0])
            #    print("Bottom-right:", coordinates[1])
            #else:
            #    print("No bounding box selected.")
            cv2.destroyAllWindows()
            break
    return list(coordinates[0] + coordinates[1])

#if __name__ == '__main__':
#    image_path = 'download.png'  # Provide the image file path here
#    coordinates = main(image_path)
#    print(coordinates)
