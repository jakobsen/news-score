import { useState } from "react";
import "./App.css";
import { Button } from "./components/Button";
import { Input } from "./components/Input";
import { calculateScore } from "./api/news";
import { Card } from "./components/Card";

function App() {
  const [temperature, setTemperature] = useState("");
  const [heartRate, setHeartRate] = useState("");
  const [respiratoryRate, setRespiratoryRate] = useState("");
  const [score, setScore] = useState<number | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const measurements = {
      temperature: Number(temperature),
      heartRate: Number(heartRate),
      respiratoryRate: Number(respiratoryRate),
    };
    const result = await calculateScore(measurements);
    setScore(result.score);
  };

  const handleReset = () => {
    setTemperature("");
    setHeartRate("");
    setRespiratoryRate("");
    setScore(null);
  };

  return (
    <main>
      <h1>NEWS score calculator</h1>
      <form onSubmit={handleSubmit}>
        <Input
          id="body-temp"
          label="Body temperature"
          subLabel="Degrees celcius"
          value={temperature}
          onChange={(e) => setTemperature(e.target.value)}
          type="number"
          inputMode="numeric"
        />
        <Input
          id="heart-rate"
          label="Heartrate"
          subLabel="Beats per minute"
          value={heartRate}
          onChange={(e) => setHeartRate(e.target.value)}
          type="number"
          inputMode="numeric"
        />
        <Input
          id="respiratory-rate"
          label="Respiratory rate"
          subLabel="Breaths per minute"
          value={respiratoryRate}
          onChange={(e) => setRespiratoryRate(e.target.value)}
          type="number"
          inputMode="numeric"
        />
        <div className="actions">
          <Button>Calculate NEWS score</Button>
          <Button type="reset" variant="secondary" onClick={handleReset}>
            Reset form
          </Button>
        </div>
      </form>
      {score !== null && (
        <Card>
          News score: <span style={{ fontWeight: 600 }}>{score}</span>
        </Card>
      )}
    </main>
  );
}

export default App;
