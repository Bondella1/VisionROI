const DashDashboard = () => {
  // Replace with the public URL provided by Codespaces for port 8050.
  
  const dashUrl = import.meta.env.VITE_DASH_APP_URL;
  return (
    <div style={{ width: '100%', height: '100vh' }}>
      <iframe
        src={dashUrl}
        style={{ width: '100%', height: '100%', border: 'none' }}
        title="ROI Calculator Dashboard"
      />
    </div>
  );
};

export default DashDashboard;


