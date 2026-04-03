import { BrowserRouter, Routes, Route } from 'react-router';
import { Layouts } from './layouts/Layouts';
import { HomePage, CatalogPage, NewsPage, SwipePage } from './pages/index';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layouts />}>
          <Route index element={<HomePage />} />
          <Route path="swipe" element={<SwipePage />} />
          <Route path="news" element={<NewsPage />} />
          <Route path="catalog" element={<CatalogPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
