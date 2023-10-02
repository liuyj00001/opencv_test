while True:
    img=
    hsv=
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars",640,240)
    h_min = cv2.getTrackbarPos("Hue Min", " TrackBars ",0,179,empty)
    h_max = cv2.getTrackbarPos("Hue Max ", "TrackBars ",179,179,empty)
    s_min = cv2.getTrackbarPos("Sat Min", " TrackBars ",0,255,empty)
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars ",255,255,empty)
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars ",0,255,empty)
    v_max = cv2.getTrackbarPos("val Max", " TrackBars",255,255,empty)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)

    cv2.imshow("",)
    cv2.imshow("", )
    cv2.imshow("",)



