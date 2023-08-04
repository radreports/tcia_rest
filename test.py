import numpy as np
import numpy.ma as ma
import nibabel as nib
import nrrd


mask1, header = nrrd.read("./data/case_01/case_01_OAR_Cricopharyngeus.seg.nrrd")
# nii = nib.load("./data/case_01/case_01_OAR_Cricopharyngeus.seg.nrrd")
# mask1 = nii.get_fdata()
# mask1 = np.ma.make_mask([0, 0, 1, 0, 0])

mask2, header = nrrd.read("./data/case_01/case_01_OAR_Glottis.seg.nrrd")
# nii = nib.load("./data/case_01/case_01_OAR_Glottis.seg.nrrd")
# mask2 = nii.get_fdata()

# mask2 = np.ma.make_mask([0, 1, 0, 1, 0])

comb_mask = np.ma.mask_or(mask1, mask2)
# print("Result...",np.ma.mask_or(mask1, mask2))

# print("Result...",np.ma.mask_or(mask1, mask2))

new_image = nib.Nifti1Image(comb_mask, affine=np.eye(4))

nib.save(new_image, os.path.join('./', 'test4d.nii.gz'))  