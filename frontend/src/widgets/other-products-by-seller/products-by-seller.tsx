import React from 'react'
import { useTranslation } from 'react-i18next'

import { ScrollableProductList } from '@/widgets/scrollable-product-list/scrollable-product-list.tsx'
import { useLatestProducts } from '@/entities/product/library/hooks/use-latest-products.tsx'
import { ProductSliderSkeleton } from '@/shared/ui/skeletons'

export interface SellerProductProps {
  onProductClick: (slug: string) => void
}

export const ProductsBySeller: React.FC<SellerProductProps> = ({
  onProductClick,
}) => {
  const { t } = useTranslation()
  const { data, cursor } = useLatestProducts({
    Skeleton: <ProductSliderSkeleton />,
  })

  return (
    <ScrollableProductList
      title={t('title.productsBySeller')}
      data={data}
      cursor={cursor}
      scrollStep={3} // Number of items to scroll
      className='absolute flex w-[107%] overflow-hidden'
      onProductClick={onProductClick}
    />
  )
}
