import * as z from "zod";

const BASE_PATH = "http://localhost:8000";
const DEFAULT_HEADERS = {
  "content-type": "application/json",
  accept: "application/json",
};

interface Measurements {
  temperature: number;
  heartRate: number;
  respiratoryRate: number;
}

const NewsScore = z.object({
  score: z.number().min(0),
});
type NewsScore = z.infer<typeof NewsScore>;

export async function calculateScore({
  temperature,
  heartRate,
  respiratoryRate,
}: Measurements): Promise<NewsScore> {
  const path = `${BASE_PATH}/calculate-score`;
  const payload = {
    measurements: [
      { type: "TEMP", value: temperature },
      { type: "RR", value: respiratoryRate },
      { type: "HR", value: heartRate },
    ],
  };
  const response = await fetch(path, {
    method: "POST",
    headers: DEFAULT_HEADERS,
    body: JSON.stringify(payload),
  });
  const json = await response.json();
  return NewsScore.parseAsync(json);
}
