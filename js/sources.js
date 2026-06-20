// Vetted sources and citations for question attributions
const SOURCES = [
  { name: 'AAMC Official Guide', url: 'https://students-residents.aamc.org/' },
  { name: 'Khan Academy: MCAT', url: 'https://www.khanacademy.org/test-prep/mcat' },
  { name: 'Kaplan MCAT Prep', url: 'https://www.kaptest.com/mcat' },
  { name: 'Princeton Review MCAT', url: 'https://www.princetonreview.com/medical/mcat-test-prep' },
  { name: 'UWorld MCAT', url: 'https://www.uworld.com/mcat/' },
  { name: 'OpenStax Biology', url: 'https://openstax.org/details/books/biology-2e' },
  { name: 'PubMed Reviews', url: 'https://pubmed.ncbi.nlm.nih.gov/' }
];

// lightweight fallback for `pick` if scripts load out of order
if (typeof pick !== 'function') {
  window.pick = (items, index) => items[index % items.length];
}
