import cv2.cv as cv
import cv2
import socket

if _name_ == "_main_":
    udp =socket.socket(soclet.AF_INET,socket.SOCK_DGRAM)

    capture =cv.CaptureFromCAM(0)
    cv.NamedWindow("ClientCAM",1)
    cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_WIDTH,320)
    cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_HEIGHT,240)
    
    while True:
        img =cv.QueryFrame(capture)
        jpgstring =cv.EncodeImage(".jpeg",img).tostring()
        cv.ShowImage("ClientCAM",img)
        udp.sendto(jpgstring,("198.168.0.140",#port#))
                              if cv.WaitKey(10) ==27:
                              break

                              cv.DestroyAllWindows()
                              udp.close()
        
        
    
