<!-- title: Hand Brake CLI reference -->


Rips the first track from the DVD mounted on /dev/sr0

    hbc -t 1 -i /dev/sr0 -o PersonOfInterestS2D3.mp4 -e mpeg4 -b 1000 -B 192

List all available tracks on the DVD mounted on /dev/sr0

    hbc -t 0 -i /dev/sr0 -o PersonOfInterestS2D3.mp4 -e mpeg4 -b 1000 -B 192

where ...

* -t = track number
* -i = input media
* -o = output media
* -e = encoding engine
* -b = video bit rate
* -B = audio bit rate
