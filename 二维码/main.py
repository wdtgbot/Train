import qrcode

qr = qrcode.QRCode(
    version=20,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('wxp://f2f1x-TSsxgI8u0Pmy38yRwN1jFfOb1pRh50wOCMG2o3aqqindRIm07mW3WwpOMIaaWZ')
qr.print_ascii(invert=True)
