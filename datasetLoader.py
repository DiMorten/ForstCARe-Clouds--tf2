class DatasetLoader():
    def loadSar(load_fn, path):
        sar_vv = load_tiff_image(obj.sar_path + obj.sar_name[0] + '.tif').astype('float32')
        sar_vh = load_tiff_image(obj.sar_path + obj.sar_name[1] + '.tif').astype('float32')
        sar = np.concatenate((np.expand_dims(sar_vv, 2), np.expand_dims(sar_vh, 2)), axis=2)
        del sar_vh, sar_vv
        return sar        


class SaLoader(DatasetLoader):
    def loadSar(load_fn, path):
        sar = load_tiff_image(obj.sar_path + obj.sar_name[0] + '.tif').astype('float32')
        return sar

