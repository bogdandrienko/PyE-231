export function Loader1({ isView }: any) {
  return (
    <div>
      {isView && (
        <div className="spinner-border text-secondary" role="status">
          <span className="visually-hidden">...</span>
        </div>
      )}
    </div>
  );
}
