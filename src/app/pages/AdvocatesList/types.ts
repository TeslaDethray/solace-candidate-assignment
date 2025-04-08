export enum DegreeType {
  MD = 'MD',
  MSW = 'MSW',
  PHD = 'PhD',
}

export enum SpecialtyType {
  ADHD = "Attention and Hyperactivity (ADHD)",
  ADHD_TESTING = "Neuropsychological evaluations & testing (ADHD testing)",
  BIPOLAR = "Bipolar",
  COACHING = "Coaching (leadership, career, academic and wellness)",
  DIABETES = "Diabetic Diet and nutrition",
  DOMESTIC_ABUSE = "Domestic abuse",
  EATING_DISORDER = "Eating disorders",
  GENERAL = "General Mental Health (anxiety, depression, stress, grief, life transitions)",
  GROWTH = "Personal growth",
  LEARNING_DISORDER = "Learning disorders",
  LGBTQ = "LGBTQ",
  LIFE_COACHING = "Life coaching",
  MEDICATION = "Medication/Prescribing",
  MENS = "Men's issues",
  OCD = "Obsessive-compulsive disorders",
  PAIN = "Chronic pain",
  PEDIATRIC = "Pediatrics",
  PERSONALITY_DISORDER = "Personality disorders",
  PTSD = "Trauma & PTSD",
  RELATIONSHIP = "Relationship Issues (family, friends, couple, etc)",
  SCHIZOPHRENIA_PSYCHOSIS = "Schizophrenia and psychotic disorders",
  SLEEP = "Sleep issues",
  SUBSTANCE_ABUSE = "Substance use/abuse",
  SUICIDE = "Suicide History/Attempts",
  WEIGHT = "Weight loss & nutrition",
  WOMEN = "Women's issues (post-partum, infertility, family planning)",
}

export type AdvocateType = {
  city: string;
  degree: DegreeType;
  firstName: string;
  lastName: string;
  specialties: Array<SpecialtyType>;
  yearsOfExperience: number;
  phoneNumber: string;
};
