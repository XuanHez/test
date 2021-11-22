#!/usr/bin/env python
# coding: utf-8

# In[22]:


VIDEO_IN = cv2.VideoCapture(0)
while True:
    hasFrame, img = VIDEO_IN.read()
    img = cv2.resize(img, None, fx=0.5, fy=0.5)
    img = face_check(img)
    cv2.imshow("Frame", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
VIDEO_IN.release()
cv2.destroyAllWindows()


# In[ ]:




