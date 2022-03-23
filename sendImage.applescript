on run {phoneNumber, imagePath}
    tell application "Messages"
        set parameters to 1st service whose service type = iMessage
        set person to buddy phoneNumber of parameters
        set newFile to (imagePath as POSIX file)
        send newFile to person
    end tell
end run
