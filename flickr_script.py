with open train

def get_nb_files(directory):
  """Get number of files by searching directory recursively"""
  if not os.path.exists(directory):
    return 0
  cnt = 0
  for r, dirs, files in os.walk(directory):
    for dr in dirs:
      cnt += len(glob.glob(os.path.join(r, dr + "/*")))
  return cnt

nb_samples = get_nb_files(args.val_dir)


for i in range()

    count
    egex ^ 0000000?i *.mask0 *
    del *.

if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--sample_dir")

