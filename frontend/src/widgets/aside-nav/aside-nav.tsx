import { ChevronRight } from 'lucide-react'
import { useTranslation } from 'react-i18next'
import { Link, useNavigate } from 'react-router-dom'

import { useCategories } from '@/entities/category/library/hooks/use-categories.tsx'
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from '@/shared/ui/shadcn-ui/hover-card.tsx'
import {
  Menubar,
  MenubarContent,
  MenubarItem,
  MenubarMenu,
  MenubarTrigger,
} from '@/shared/ui/shadcn-ui/menubar.tsx'
import { Separator } from '@/shared/ui/shadcn-ui/separator'
import { FacebookIconOutline, InstagramIconOutline } from '@/shared/ui'
import { AsideCategorySkeleton } from '@/shared/ui/skeletons'
import { capitalizeFirstWord } from '@/shared/library/utils/capitalize-first-word.ts'

const TITLE_LENGTH_THRESHOLD = 17 // Set a threshold for truncation (number of characters)
const SUBTITLE_LENGTH_THRESHOLD = 15

export const AsideNav = ({ onCloseMenu }: { onCloseMenu?: () => void }) => {
  const { t } = useTranslation()
  const navigate = useNavigate()

  const { categories, cursor } = useCategories({
    Skeleton: <AsideCategorySkeleton />,
  })

  const handleCategoryClick = (path: string) => {
    navigate(`/catalog/${path}`)
    onCloseMenu && onCloseMenu()
  }

  return (
    <aside className='w-[305px] pl-[18px] pr-0'>
      <Menubar className='h-auto rounded-none border-0 p-0'>
        {cursor}
        <ul className='max-w-[287px] space-y-1'>
          {categories?.map(cat => (
            <li key={cat.path}>
              <MenubarMenu key={cat.path}>
                <MenubarTrigger
                  onClick={() => {
                    onCloseMenu && handleCategoryClick(cat.path)
                  }}
                  className='group flex w-full cursor-pointer items-center justify-between gap-3 rounded-[81px] border-0 py-[6px] pl-2 pr-0 text-base/4 font-normal transition-colors duration-300 hover:bg-primary-900 hover:text-gray-50 data-[state=open]:bg-primary-900 data-[state=open]:text-gray-50'
                >
                  {cat.icon ? (
                    <img
                      src={cat.icon}
                      alt={cat.title}
                      className='h-6 w-6 transition duration-300 ease-in-out focus:brightness-0 focus:invert focus:filter group-hover:brightness-0 group-hover:invert group-hover:filter group-data-[state=open]:brightness-0 group-data-[state=open]:invert group-data-[state=open]:filter'
                    />
                  ) : null}
                  <p className='flex-1 truncate text-start text-base'>
                    {cat.title}
                  </p>
                  <ChevronRight />
                </MenubarTrigger>
                <MenubarContent
                  side='right'
                  sideOffset={15}
                  className='hidden max-w-[900px] grid-cols-3 gap-[50px] rounded-[15px] border-none bg-background px-[75px] py-12 text-foreground shadow-[1px_1px_5px_0_rgba(78,78,78,0.19)] xl:grid'
                >
                  {cat.children.slice(0, 6).map(sub => (
                    <div key={sub.path} className='max-w-[155px] space-y-5'>
                      <Link to={`/catalog/${sub.path}`}>
                        <HoverCard openDelay={500} closeDelay={0}>
                          <HoverCardTrigger asChild>
                            <h4 className='overflow-hidden text-ellipsis whitespace-nowrap text-base/[19.36px] font-semibold capitalize hover:text-primary-600'>
                              {sub.title}
                            </h4>
                          </HoverCardTrigger>
                          {/* Only render HoverCardContent if title length exceeds threshold */}
                          {sub.title.length > SUBTITLE_LENGTH_THRESHOLD && (
                            <HoverCardContent
                              side='top'
                              className='w-fit bg-gray-50 capitalize'
                            >
                              {sub.title}
                            </HoverCardContent>
                          )}
                        </HoverCard>
                      </Link>
                      <ul className='space-y-2.5'>
                        {sub.children.slice(0, 5).map(item => (
                          <li key={item.path}>
                            <Link to={`/catalog/${item.path}`}>
                              <MenubarItem className='max-w-[155px] cursor-pointer bg-none p-0 text-base/[19.36px] font-normal transition-colors duration-300'>
                                <HoverCard openDelay={500} closeDelay={0}>
                                  <HoverCardTrigger asChild>
                                    <p className='overflow-hidden text-ellipsis whitespace-nowrap hover:text-primary-600'>
                                      {capitalizeFirstWord(item.title)}
                                    </p>
                                  </HoverCardTrigger>
                                  {/* Only render HoverCardContent if title length exceeds threshold */}
                                  {item.title.length >
                                    TITLE_LENGTH_THRESHOLD && (
                                    <HoverCardContent
                                      side='top'
                                      className='w-fit bg-gray-50 hover:text-primary-600'
                                    >
                                      {capitalizeFirstWord(item.title)}
                                    </HoverCardContent>
                                  )}
                                </HoverCard>
                              </MenubarItem>
                            </Link>
                          </li>
                        ))}
                      </ul>
                      <div>
                        <Link
                          to={`/catalog/${sub.path}`}
                          className='rounded-[100px] bg-primary-700 px-6 py-2 text-sm text-gray-50 transition-colors duration-300 hover:bg-primary-600'
                        >
                          {t('words.showAll')}
                        </Link>
                      </div>
                    </div>
                  ))}
                </MenubarContent>
              </MenubarMenu>
            </li>
          ))}
        </ul>
      </Menubar>
      <div className='flex items-center justify-center pb-[26px] pr-[43px] pt-[19px]'>
        <Separator className='bg-gray-200' />
      </div>
      <div className='flex flex-col'>
        <p className='flex-1 pl-2.5'>{t('asideLinks.socialMedia')}</p>
        <div className='flex w-[271px] items-center gap-0 rounded-[81px] py-0.5'>
          <a
            href='#'
            aria-label='Instagram'
            className='cursor-pointer transition-colors duration-300 hover:text-primary-200'
          >
            <InstagramIconOutline />
          </a>
          <a
            href='#'
            aria-label='Facebook'
            className='cursor-pointer transition-colors duration-300 hover:text-primary-200'
          >
            <FacebookIconOutline />
          </a>
        </div>
      </div>
    </aside>
  )
}
