import random
import pandas as pd

def generate_exam_combinations(n_combinations: int,output_csv: str):
	section1_max = 2
	section2_max = 13
	section3_max = 15
		
	section1_questions = [f"S1Q{i+1}" for i in range(10)]
	section2_questions = [f"S2Q{i+1}" for i in range(5)]
	section3_questions = ["S3Q1"]
	all_questions = section1_questions + section2_questions + section3_questions
	
	valid_combinations = []
	attempts = 0
	max_attempts = n_combinations * 1000 # Increase if needed
	
	while len(valid_combinations) < n_combinations and attempts < max_attempts:
		s1 = [random.randint(0, section1_max) for _ in section1_questions]
		s2 = [random.randint(0, section2_max) for _ in section2_questions]
		s3 = [random.randint(0, section3_max) for _ in section3_questions]
		
		total = sum(s1) + sum(s2) + sum(s3)
		
		if total == 35:
			valid_combinations.append(s1 + s2 + s3)
		
		attempts += 1

	if len(valid_combinations) < n_combinations:
		print(f"Only {len(valid_combinations)} combinations generated within {max_attempts} attempts.")

	df = pd.DataFrame(valid_combinations, columns=all_questions)
	df.to_csv(output_csv, index=False)
	print(f"Saved {len(valid_combinations)} combinations to: {output_csv}")

# Example Usage

generate_exam_combinations(n_combinations = 10,output_csv = "exam_combinations_10.csv")