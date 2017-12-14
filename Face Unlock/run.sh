dbus-monitor --session "type='signal',interface='com.ubuntu.Upstart0_6'" | \
(
  while true; do
    read X
    if echo $X | grep "desktop-lock" &> /dev/null; then
      echo 'Locked'
      while true; do
      	python face_recog.py;
      	python3 face_unlock.py;
        value=$(<access.txt)
      	if [ "$value" == "True" ]; then
  			break
		fi
      done
    elif echo $X | grep "desktop-unlock" &> /dev/null; then
      echo 'Unlocked'
    fi
  done
)