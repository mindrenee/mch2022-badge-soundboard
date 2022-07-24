python3 ../mch2022-tools-master/webusb_fat_push.py __init__.py /sdcard/apps/python/soundboard/__init__.py
for s in `ls sounds`; do
	echo $s
	python3 ../mch2022-tools-master/webusb_fat_push.py sounds/$s /sdcard/apps/python/soundboard/sounds/$s
done


