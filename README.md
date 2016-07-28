#Mini Programs

##Python

###GenRandNums
Two functions are defined in this script.

GetSetOfNumbers(min, max, postFix) is used to get a grouping
of numbers with atleast the minimum number of digits no more than the max.
If the postFix parameter is true a dot is appended to the end of the group of numbers.

GenerateIp() generates an ip like the following xxx.xxx.xxx.xxx
the amount of digits in each grouping ranges from 2 to 3

    //Example usage
    from GenRandNums import GenerateIP

    ip = GenerateIp()
    print ip

Also check out it being used in randomPing

###Random Ping
Generates a random Ip using the GenRandNums script. Then makes a system call
to ping the ip address. The response is piped to a text file named PingOutput.txt on the Desktop.
If the address gets a response the file will contain <ipaddress> is up! or <ipaddress> is down!
if there is no response.
This works on Mac and maybe Linux but not windows. It doesn't work on windows 
because it uses unix style paths.

###Fizz Buzz
An interview question I saw on Quroa quickly written up in python just to see if I could do it.

###Tournament Brackets
Randomizes a list of names and then builds out a brackets for each round.

<<<<<<< HEAD
###Remove post fix
###Remove pre fix
###Rename files
=======
###WebDev 
HTML 5 canvas drawing


>>>>>>> origin/master
