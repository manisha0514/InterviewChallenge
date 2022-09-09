from PostCodeUK.postcode import PostCode

if __name__ == '__main__':
    pcObj = PostCode()
    pcName = sys.argv[1]
    pcName = pcName.upper()
    if ' ' in pcName:
        pcName = pcName.replace(" ", "")
    pcObj.validate_postcode_Regex(pcName)
    pcObj.validate_postcode(pcName)
