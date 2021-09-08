while True:\n	try:\n		t = UTC.getTime()\n	except Exception as e:\n		print(e)\n		sta_if.disconnect()\n		time.sleep(1)\n		sta_if.connect(ssid_, wp2_pass)\n		pass\n	else:\n		oled.fill(0)\n		oled.show()\n		oled.text('Gio:  '+ t['hour'], 0 ,0)\n		oled.text('Phut:  '+ t['minute'], 0 ,10)\n		oled.text('Giay:  '+ t['second'], 0 ,20)\n		oled.show()\n	time.sleep(30)\n

