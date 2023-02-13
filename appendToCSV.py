# YOU HAVE TO MANUALLY CREATE THE CSV FILE UNDER FILES (IT HAS TO BE BLANK) IN ORDER TO APPEND THE DATA INSIDE IT

name_of_csv_file = 'new_params_4_dbftresh.csv'

def append_data_to_csv(file_path, downsampling_rate, frame_length_in_s, dbFSthres, duration_thres, num_frames, num_frequency_bins, accuracy, avg_time_ms):
    fieldnames = ['id','downsampling_rate','frame_length_in_s','dbFSthres','duration_thres','accuracy','avg_time_ms', 'num_frames', "num_frequency_bins"]
    next_id = get_length_file(file_path)
    global COUNTER
    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if (COUNTER == 0):
            writer.writeheader()
            COUNTER = COUNTER + 1 #to print the headers only the first time
        writer.writerow({
            'id': next_id,
            'downsampling_rate': downsampling_rate,
            'frame_length_in_s': frame_length_in_s,
            'dbFSthres': dbFSthres,
            'duration_thres': duration_thres,
            'num_frames' : num_frames,
            'num_frequency_bins' : num_frequency_bins,
            'accuracy': accuracy,
            'avg_time_ms': avg_time_ms,
        })
