import React from 'react';

const DashEmbed = () => {
  const dashUrl = import.meta.env.VITE_DASH_APP_URL; // Vite uses import.meta.env
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

export default DashEmbed;

