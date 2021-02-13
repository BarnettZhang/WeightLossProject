import numpy as np
import pandas as pd


def load_data():
    df = pd.read_excel('../Data/Patient and Treatment Characteristics.xlsx', sheet_name='Filtered')
    LFVO = np.array(df['LFVO'].tolist())
    LFSA = np.array(df['LFSA'].tolist())
    LFSP = np.array(df['LFSP'].tolist())
    LFEC = np.array(df['LFEC'].tolist())
    LFCO = np.array(df['LFCO'].tolist())
    LFMA = np.array(df['LFMA'].tolist())
    LFME = np.array(df['LFME'].tolist())
    LFMI = np.array(df['LFMI'].tolist())
    LFST = np.array(df['LFST'].tolist())
    LFSK = np.array(df['LFSK'].tolist())
    LFEN = np.array(df['LFEN'].tolist())
    LFUN = np.array(df['LFUN'].tolist())
    LFD2 = np.array(df['LFD2'].tolist())
    LFD10 = np.array(df['LFD10'].tolist())
    LFD20 = np.array(df['LFD20'].tolist())
    LFD30 = np.array(df['LFD30'].tolist())
    LFD40 = np.array(df['LFD40'].tolist())
    LFD50 = np.array(df['LFD50'].tolist())
    LFD60 = np.array(df['LFD60'].tolist())
    LFD70 = np.array(df['LFD70'].tolist())
    LFD80 = np.array(df['LFD80'].tolist())
    LFD90 = np.array(df['LFD90'].tolist())
    LFD98 = np.array(df['LFD98'].tolist())
    LFV15 = np.array(df['LFV15'].tolist())
    LFV20 = np.array(df['LFV20'].tolist())
    LFV25 = np.array(df['LFV25'].tolist())
    LFV30 = np.array(df['LFV30'].tolist())
    LFV35 = np.array(df['LFV35'].tolist())
    LFV40 = np.array(df['LFV40'].tolist())
    LFV45 = np.array(df['LFV45'].tolist())

    RTVO = np.array(df['RTVO'].tolist())
    RTSA = np.array(df['RTSA'].tolist())
    RTSP = np.array(df['RTSP'].tolist())
    RTEC = np.array(df['RTEC'].tolist())
    RTCO = np.array(df['RTCO'].tolist())
    RTMA = np.array(df['RTMA'].tolist())
    RTME = np.array(df['RTME'].tolist())
    RTMI = np.array(df['RTMI'].tolist())
    RTST = np.array(df['RTST'].tolist())
    RTSK = np.array(df['RTSK'].tolist())
    RTEN = np.array(df['RTEN'].tolist())
    RTUN = np.array(df['RTUN'].tolist())
    RTD2 = np.array(df['RTD2'].tolist())
    RTD10 = np.array(df['RTD10'].tolist())
    RTD20 = np.array(df['RTD20'].tolist())
    RTD30 = np.array(df['RTD30'].tolist())
    RTD40 = np.array(df['RTD40'].tolist())
    RTD50 = np.array(df['RTD50'].tolist())
    RTD60 = np.array(df['RTD60'].tolist())
    RTD70 = np.array(df['RTD70'].tolist())
    RTD80 = np.array(df['RTD80'].tolist())
    RTD90 = np.array(df['RTD90'].tolist())
    RTD98 = np.array(df['RTD98'].tolist())
    RTV15 = np.array(df['RTV15'].tolist())
    RTV20 = np.array(df['RTV20'].tolist())
    RTV25 = np.array(df['RTV25'].tolist())
    RTV30 = np.array(df['RTV30'].tolist())
    RTV35 = np.array(df['RTV35'].tolist())
    RTV40 = np.array(df['RTV40'].tolist())
    RTV45 = np.array(df['RTV45'].tolist())

    percentage_bw_loss = np.array(df['PerBWLoss'].tolist())
    percentage_bw_loss = percentage_bw_loss.reshape(-1, 1)

    real_bw_loss = np.array(df['REAL_BW_LOSS'].tolist())
    bw_loss_cat = []
    for x in real_bw_loss:
        if x >= 5:
            bw_loss_cat.append(1)
        else:
            bw_loss_cat.append(0)
    bw_loss_cat = np.array(bw_loss_cat)
    bw_loss_cat = bw_loss_cat.ravel()
    feature_names = list(df.columns.values)[7:]
    X = np.transpose(np.array([LFVO, LFSA, LFSP, LFEC, LFCO, LFMA, LFME, LFMI, LFST, LFSK, LFEN, LFUN, LFD2, LFD10, LFD20,
                  LFD30, LFD40, LFD50, LFD60, LFD70, LFD80, LFD90, LFD98, LFV15, LFV20, LFV25, LFV30, LFV35,
                  LFV40, LFV45, RTVO, RTSA, RTSP, RTEC, RTCO, RTMA, RTME, RTMI, RTST, RTSK, RTEN, RTUN, RTD2, RTD10,
                  RTD20, RTD30, RTD40, RTD50, RTD60, RTD70, RTD80, RTD90, RTD98, RTV15, RTV20, RTV25, RTV30, RTV35,
                  RTV40, RTV45]))

    return X, percentage_bw_loss, bw_loss_cat, feature_names
