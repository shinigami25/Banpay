import { useEffect, useState } from "react";
import api from "../api";

export default function GhibliPage() {
  const [ghibliData, setGhibliData] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const { data } = await api.get("/ghibli/");
        setGhibliData(data);
      } catch (err) {
        setError(err.response?.data?.detail || "Failed to load Ghibli data");
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <div style={styles.error}><h2>Access Denied</h2><p>{error}</p></div>;
  if (!ghibliData) return null;

  return (
    <div>
      <h2>Ghibli — {ghibliData.resource}</h2>
      <div style={styles.grid}>
        {ghibliData.data.map((item, i) => (
          <div key={item.id || i} style={styles.card}>
            <h3 style={styles.cardTitle}>{item.name || item.title}</h3>
            {item.description && <p style={styles.cardText}>{item.description}</p>}
            {item.director && <p style={styles.meta}>Director: {item.director}</p>}
            {item.release_date && <p style={styles.meta}>Year: {item.release_date}</p>}
            {item.classification && <p style={styles.meta}>Classification: {item.classification}</p>}
            {item.terrain && <p style={styles.meta}>Terrain: {item.terrain}</p>}
            {item.vehicle_class && <p style={styles.meta}>Class: {item.vehicle_class}</p>}
            {item.gender && <p style={styles.meta}>Gender: {item.gender}</p>}
            {item.age && <p style={styles.meta}>Age: {item.age}</p>}
          </div>
        ))}
      </div>
    </div>
  );
}

const styles = {
  error: {
    textAlign: "center",
    marginTop: "60px",
    color: "#e94560",
  },
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fill, minmax(280px, 1fr))",
    gap: "16px",
  },
  card: {
    background: "#f8f9fa",
    borderRadius: "8px",
    padding: "20px",
    border: "1px solid #e0e0e0",
  },
  cardTitle: { margin: "0 0 8px" },
  cardText: { fontSize: "14px", color: "#555", margin: "0 0 8px" },
  meta: { fontSize: "13px", color: "#777", margin: "4px 0" },
};
